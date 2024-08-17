import httpx
from faker import Faker
from pydantic import BaseModel
import pytest
from typing import Optional

# Model definitions
class Product(BaseModel):
    nome: str
    preco: int
    descricao: str
    quantidade: int

class CreateResponse(BaseModel):
    id: str
    message: str

class ProductResponse(BaseModel):
    id: str
    nome: str
    preco: int
    descricao: str
    quantidade: int

class Login(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    message: str
    token: str

class User(BaseModel):
    nome: str
    email: str
    password: str
    administrador: str

class UserResponse(BaseModel):
    id: str
    nome: str
    email: str
    password: str
    administrador: str

class TestProduct:
    BASE_URL = "https://serverest.dev"
    
    def setup(self):
        self.faker = Faker("pt_BR")
        self.client = httpx.AsyncClient()

    @pytest.mark.asyncio
    async def test_given_new_product_when_try_save_should_save_successfully(self):

        product = Product(
            nome=self.faker.commerce_product_name(),
            preco=int(self.faker.commerce_price(1, 1000, 0, "")),
            descricao=self.faker.commerce_product_description(),
            quantidade=int(self.faker.commerce_price(1, 100, 0, ""))
        )
        json_data = product.json()
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {await self.generate_token()}"}

        response = await self.client.post(f"{self.BASE_URL}/produtos", content=json_data, headers=headers)

        assert response.status_code == 201
        response_data = response.json()
        create_response = CreateResponse(**response_data)

        assert create_response.id is not None
        assert create_response.message == "Cadastro realizado com sucesso"

        product_id = create_response.id
        get_product_response = await self.client.get(f"{self.BASE_URL}/produtos/{product_id}")

        assert get_product_response.status_code == 200
        product_response_data = get_product_response.json()
        product_response = ProductResponse(**product_response_data)

        assert product_response.id == product_id
        assert product_response.nome == product.nome
        assert product_response.descricao == product.descricao
        assert product_response.quantidade == product.quantidade
        assert product_response.preco == product.preco

    async def generate_token(self) -> str:
        user = await self.create_user()

        login = Login(
            email=user.email,
            password=user.password
        )
        json_data = login.json()
        headers = {"Content-Type": "application/json"}

        response = await self.client.post(f"{self.BASE_URL}/login", content=json_data, headers=headers)

        assert response.status_code == 200
        response_data = response.json()
        token_response = TokenResponse(**response_data)

        assert token_response.token is not None
        assert token_response.message == "Login realizado com sucesso"

        return token_response.token

    async def create_user(self) -> User:
        user = User(
            nome=self.faker.name(),
            email=self.faker.email(),
            password=self.faker.password(),
            administrador="true"
        )
        json_data = user.json()
        headers = {"Content-Type": "application/json"}

        response = await self.client.post(f"{self.BASE_URL}/usuarios", content=json_data, headers=headers)

        assert response.status_code == 201

        return user

    def teardown(self):

        self.client.aclose()
