import httpx
from faker import Faker
from pydantic import BaseModel
import pytest

# Model definitions
class User(BaseModel):
    nome: str
    email: str
    password: str
    administrador: str

class CreateResponse(BaseModel):
    id: str
    message: str

class UserResponse(BaseModel):
    id: str
    nome: str
    email: str
    password: str
    administrador: str

class TestUser:
    def setup(self):
        self.faker = Faker("pt_BR")
        self.base_url = "https://serverest.dev/"
        self.client = httpx.AsyncClient()

    @pytest.mark.asyncio
    async def test_given_new_user_when_try_save_should_save_successfully(self):

        user = User(
            nome=self.faker.name(),
            email=self.faker.email(),
            password=self.faker.password(),
            administrador="true",
        )
        json_data = user.json()
        headers = {"Content-Type": "application/json"}

        response = await self.client.post(f"{self.base_url}/usuarios", content=json_data, headers=headers)

        assert response.status_code == 201
        response_data = response.json()
        create_response = CreateResponse(**response_data)

        assert create_response.id is not None
        assert create_response.message == "Cadastro realizado com sucesso"

        user_id = create_response.id
        get_user_response = await self.client.get(f"{self.base_url}/usuarios/{user_id}")

        assert get_user_response.status_code == 200
        user_response_data = get_user_response.json()
        user_response = UserResponse(**user_response_data)

        assert user_response.id == user_id
        assert user_response.nome == user.nome
        assert user_response.email == user.email
        assert user_response.password == user.password
        assert user_response.administrador == user.administrador

    def teardown(self):

        self.client.aclose()
