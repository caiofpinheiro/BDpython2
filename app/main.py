from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando usuário
    service.criar_usuario("Caio", "caiooo@gmail.com", "1234")

    
    # Listando todos os usuários.
    print("Listando todos os usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() # Chamada para função.

