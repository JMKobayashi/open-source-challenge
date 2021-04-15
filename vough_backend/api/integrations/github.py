import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        # Criando a URL para a chamada de API do Github
        url = self.API_URL+"/orgs/"+login

        # Realizando a chamada de API
        result = requests.get(url)

        # Verificando o status da resposta
        # Se for 200
        if(result.status_code == 200):
            # Transforma o texto da resposta em JSON
            result = result.json()

            # Tenta pegar o nome no JSON de resposta
            try:
                name = result['name']
            # Se der KeyError coloca como nome o login
            except KeyError:
                name = ""

            # Gera um dicionário com o login, nome e quantidade de repositórios
            # públicos da organização
            data = {"login":result['login'], "name":name, "public_repos":result['public_repos']}

            # Retorna o status e os dados da resposta
            return {"status":200,"data":data}

        # Se for diferente de 200
        else:
            # Retorna o status 404 (padrão de resposta da API do Github) e o campo data como None
            return {"status":404,"data":None}


    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        # Criando a URL para a chamada de API do Github
        url = self.API_URL+"/orgs/"+login+"/public_members"

        # Realizando a chamada de API
        result = requests.get(url)

        # Verificando o status da resposta
        # Se for 200
        if(result.status_code == 200):
            # Transforma o texto da resposta em JSON
            result = result.json()

            # Retorna o tamanho
            return len(result)

        # Se for diferente de 200
        else:
            # Retorna o status 404 (padrão de resposta da API do Github) e o campo data como None
            return None
