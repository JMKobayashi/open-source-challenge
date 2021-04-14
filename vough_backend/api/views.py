from rest_framework import viewsets, status
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet que contém toda a manipulação da API da listagem de organizações de
    interesse do usuário. Possui também o histórico das organizações
    pesquisadas e a possibilidade de remover organizações do histórico usando
    o login.

    Parameters
    ----------
    login : str
        O login da organização de interesse do usuário.

    Methods
    -------
    retrieve(login=None)
        Busca no banco de dados os detalhes de uma organização específica.
    """
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def retrieve(self, request, login=None):

        # Procura o login da organização no banco de dados
        organization = models.Organization.objects.filter(login=login)

        # Se não encontrar a organização no banco de dados
        if not organization:

            # Instacia a classe da API do Github
            github = GithubApi()
            # Chama a API de busca de organização passando o login como atributo
            organization = github.get_organization(login)

            # Se a organização não for encontrada pela API do Github
            if organization['status'] == 404:

                # Retorna o status de erro 404
                return Response(status=404)

            # Caso encontre a organização pela API do Github
            else:

                # Pega a quantidade de repositórios publicos da organização
                repos = organization['data']['public_repos']
                # Chama a API para buscar a quantidade de membros públicos da organização
                members = github.get_organization_public_members(login=login)
                # Soma a quantidade de repositórios e a quantidade membros
                # para obter o score da organização
                score = repos+members

                # Cria um dicionário para passar os dados para o serializador
                data = {'login':login, 'name':organization['data']['name'], 'score':score}

                # Passa a variável para o serializador
                serializer_result = serializers.OrganizationSerializer(data=data)

                # Se o resultado for válido
                if serializer_result.is_valid(True):

                    # Salva a nova organização pesquisada no banco
                    serializer_result.save()

                # Retorna uma resposta com os dados da organização e o status 200
                return Response(data=serializer_result.data,status=organization['status'])

        # Caso encontre a organização
        else:

            # Passa a organização para o serializador
            serializer_result = serializers.OrganizationSerializer(organization,many=True)

            # Retorna uma resposta com os dados da organização e o status 200
            return Response(data=serializer_result.data,status=200)
