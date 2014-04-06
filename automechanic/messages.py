# -*- coding:utf-8 -*-
'''
@author:: Mateus Constanzo
@organization: S2it
@copyright: 2013 globo.com todos os direitos reservados.
'''

user_label = 'Usuário'
password_label = 'Senha'


error_messages = {
    'required':             u'Este campo é obrigatório.',
    'max_length':           u'Este campo tem que ter no máximo %(limit_value)s caracteres.',
    'min_length':           u'Este campo tem que ter no mínimo %(limit_value)s caracteres.',
    'invalid_choice':       u'Opção inválida selecionada.',
    'can_not_remove_all':   u'Não foi possível excluir nenhum dos itens selecionados.',
    'can_not_remove':       u'Não foi possível excluir alguns dos itens selecionados: %s.',
    'can_not_remove_error': u'A exclusão dos itens selecionados não foi concluída.',
    'select_one':           u'Nenhum item foi selecionado.',
    'invalid_param':        u'Valor do %s nulo ou inválido.',
    'invalid':              u'%s inválido ou não cadastrado.',
    'default_error':        u'Falha ao acessar a fonte de dados.',
    'not_registered':       u'Este registro não está cadastrado.',
    'can_not_hide_all':     u'Não foi possível ocultar nenhum dos itens selecionados.',
    'can_not_hide':         u'Não foi possível ocultar alguns dos itens selecionados: %s.',
    'can_not_hide_error':   u'A ocultação dos itens selecionados não foi concluída.',
    'duplicated':           u'Já existe um %s cadastrado com as mesmas características.',
    'can_not_remove':       u'Não foi possível excluir algum(ns) item(ns).',
    'http_error':           u'Erro ao realizar requisição REST com o SERVICE.',
    'http_error':           u'Erro ao realizar requisição REST com o SERVICE.',
    'no_permission':        u'Usuário não autorizado para acessar/executar esta operação. ',
    'communication_error':  u'Erro ao realizar comunicação com o serviço %s.',
    '404':                  u'Página não encontrada.',
    '500':                  u'Ocorreu um erro interno. Por favor contate o administrador do sistema.',
    'min_length_search':    u'É necessário informar no mínimo %s caracteres para realizar a busca.',
    'max_length_search':    u'É necessário informar no máximo %s caracteres para realizar a busca.',
}

success_messages = {
    'success_remove':       u'Todos os itens selecionados foram removidos com sucesso.',
    'success_hide':       u'Todos os itens selecionados foram ocultados com sucesso.',
    'success_insert':       u'Cadastro realizado com sucesso.',
    'success_edit':         u'Edição realizada com sucesso.',
    'success_remove_single': u'Remoção realizada com sucesso.',
}


user_messages = {
    'invalid_user':         u'Usuário inválido ou não cadastrado.',
    'invalid_pass':         u'Senha inválida.',
    'invalid_user_or_pass': u'Usuário e/ou senha inválida.',
    'inactive_user':        u'Usuário inativo ou excluído.',
    'duplicated_username':  u'Já existe um usuário cadastrado com username "%s".',
    'not_authenticated':    u'Usuário não autenticado.',
    'ldap_offline':         u'O LDAP não está disponível, não será possível realizer login com um usuário do LDAP.',

    'success_link':         u'Usuário vinculado a um contato com sucesso.',
    'error_link':           u'Não foi possível vincular o contato ao usuário.',
    'already_linked':       u'Seu usuário já está vinculado a algum contato.',
    'someone_is_already_linked': u'O usuário %s já está vinculado ao contato %s.',
    'success_create_and_link': u'O contato foi criado e vinculado ao usuário com sucesso.',
    'edit_profile_not_available': u'Esta funcionalidade só estará disponível após o vínculo do seu usuário com este contato for aprovado.',

    'invalid_basic_header': u'Cabeçalho básico inválido.',
    'invalid_token_header': u'Cabeçalho de token inválido.',
    'invalid_token':        u'Token inválido.',

    'not_vinculed_contact' : u'O usuário logado não está mais vinculado a um contato.',
}

menu_messages = {
    'duplicated_title':     u'Já existe um menu cadastrado com título "%s".',
    'invalid_parent':       u'O menu não pode ser filho dele mesmo.',
}

group_messages = {
    'duplicated_title':     u'Já existe um grupo cadastrado com nome "%s".',
}

permission_messages = {
    'invalid':              u'Permissão inválida ou não cadastrada.',
}

functionality_messages = {
    'all_picked':           u'Todas as funcionalidades do sistema já foram cadastradas para esse grupo.',
}

departments_messages = {
    'all_picked':           u'Não existem departamentos cadastrados no sistema.',
}

ldap_messages = {
    'connection_error':     u'Não foi possível comunicar com o servidor de LDAP.',
}

department_messages = {
    'duplicated_name':     u'Já existe um departamento cadastrado com nome "%s".',
}

area_messages = {
    'duplicated_name':     u'Já existe uma área cadastrada com nome "%s".',
    'invalid':              u'Área inválida ou não cadastrada.',
}

phone_messages = {
    'required_fields':  u'Todos os campos do Telefone devem ser preenchidos.',
    'invalid_format':   u'Existe(m) telefone(s) com formato(s) inválido(s).',
}

contact_messages = {
    'max_length':           u'Este campo tem que ter no máximo %(limit_value)s caracteres.',
    'min_length':           u'Este campo tem que ter no mínimo %(limit_value)s caracteres.',
    'invalid':              u'Digite um endereço de e-mail válido.',
    'contact_invalid':      u'Você cadastrou uma equipe com contato(s) que está(ão) oculto(s).',
    'invalid_cpf':          u'Cpf inválido.',
    'contact_does_not_exists': u'O contato selecionado não existe.',
    'invalid_date': u'Data inválida.',
}

vacation_messages = {
    'invalid':              u'Data inválida.',
    'invalid_start_date':   u'A data inicial não pode ser maior que a data final.',
}

shift_messages = {
    'max_length':           u'Este campo tem que ter no máximo %(limit_value)s caracteres.',
    'min_length':           u'Este campo tem que ter no mínimo %(limit_value)s caracteres.',
    'invalid':              u'Digite um horário válido.',
    'duplicate':            u'Já existe um turno cadastrado com esse valores para essa equipe.',
    'can_not_remove':       u'Não foi possível excluir algum(ns) item(ns) pois o(s) mesmo(s) possui(em) vínculo com alguma escala ou exceção.',
    'can_not_update':       u'Não foi possível alterar o Turno pois o mesmo possui vínculo com alguma escala ou exceção. Nesse caso, apenas o nome pode ser alterado.'
}

team_messages = {
     'invalid':              u'Equipe inválida ou não cadastrada.',
     'duplicated_name':     u'Já existe uma equipe cadastrada com nome "%s".',
     'invalid_param':        u'Valor da equipe nulo ou inválido.',
     'invalid_void':        u'Não existe(m) equipe(s) cadastrada(s).',
}

scale_messages = {
      'required_fields_journey': u'Os campos Dias da semana e Turno são obrigatórios.',
      'required_fields_exception': u'Os campos Início e Turno são obrigatórios.',
      'invalid_date_exception' : u'A data da exceção não pode ser menor que a data de início da Escala.',
      'invalid_last_date' : u'A data final não pode ser menor que a data inicial.',
      'duplicate_exception' : u'Já existe uma exceção cadastrada para essa escala com os valores Início: %s, Fim: %s e Turno: %s.',
      'invalid_scale':  u'Escala inválida ou não cadastrada.',
      'invalid': u'Data inválida.',
      'duplicate_exception' : u'Já existe uma exceção cadastrada para essa escala com os valores Início: %s, Fim: %s e Turno: %s.',
      'duplicate_start_date' : u'Já existe uma data inicial igual cadastrada para este mesmo contato nessa equipe.',
      'invalid_last_date_exception' : u'A data final da exceção não pode ser maior que a data de inicio da próxima escala (%s).',
      'required_shift' : u'Essa equipe não possui nenhum turno cadastrado.',
      'max_length' : u'O campo Anotações tem que ter no máximo 512 caracteres.',
      'max_category_length': u'O campo Categoria deve ter no máximo 128 caracteres.',
      'min_category_length': u'O campo Categoria deve ter no mínimo 2 caracteres.',
      'invalid_week_day': u'Foi(ram) selecionado(s) dia(s) que não está(ão) relacionado(s) ao turno selecionado.',
}

bankhours_messages = {
    'max_length':           u'Este campo tem que ter no máximo %(limit_value)s caracteres.',
    'min_length':           u'Este campo tem que ter no mínimo %(limit_value)s caracteres.',
    'invalid':              u'Quantidade de hora(s) inválida(s).',
    'invalid_param':        u'Valor do %s nulo ou inválido.',
    'totalize_success':     u'Horas totalizadas com sucesso.',
    'launch_hours':         u'Adicionando %s hora(s) - ESCALA %s: %s hora(s) trabalhada(s).',
    'no_launch_hours':      u'Adicionando %s hora(s) - ESCALA %s: %s hora(s) trabalhada(s). Obs. existe(m) horas não contabilizadas.',
    'launch_ivalid':        u'Este contato já possui horas lançadas para este mês.',
}

exception_messages = {

    'invalid_param':        u'Valor da Exceção nulo ou inválido.',
    'invalid':              u'Exceção inválida ou não cadastrada.',
    'required_shift_and_scale' : u'É necessário que o contato esteja em uma equipe com pelo menos um turno e uma escala cadastrados.',
}

holiday_messages = {
    'invalid':       u'Data ou formato de data inválido.',
    'invalid_choice':u'Ano inválido.',
}

search_messages = {
    'required':             u'Informe a palavra chave no campo de busca para exibir resultados.',
    'invalid_table':        u'Valor da tabela nulo ou inválida.',
}

date_messages = {
       'invalid':              u'Data inválida.',
       'required':             u'Este campo é obrigatório.',
}

document_messages = {
        'invalid_extension':    u'Extensão "%s" inválida.',
        'invalid':              u'Arquivo inválido ou não cadastrado.',
        'invalid_documents':    u'Arquivo(s) com extensão(ões) inválida(s):',
        'success_delete':       u'Arquivo excluído com sucesso.',
        'invalid_upload':       u'O arquivo "%s" não pode ser carregado.',
        'invalid_param':        u'Valor do %s nulo ou inválido.',
        'invalid_download':     u'Diretório inválido ou arquivo não cadastrado.',
}

dashboard_messages = {
        'invalid_style' : u'Não foi possivel salvar o estado do dashboard. Formatação de estilos inválida.',
        'success_clone' : u'Dashboard clonado com sucesso.',
        'success_shared' : u'Dashboard compartilhado com sucesso.',
        'success_unlink': u'Dashboard desvinculado com sucesso.',
        'required': u'Este campo é obrigatório para dashboard público.',
}

favorite_messages = {

        'max_length_nome' : u'O campo Nome tem que ter no máximo 45 caracteres.',
        'max_length_url' : u'O campo Url tem que ter no máximo 500 caracteres.',
        'required':    u'Exite(m) campo(s) não preenchido(s)' ,
}

service_now_messages = {

    'required':             u'Existe(m) campo(s) obrigatório(s) não preenchido(s).',
    'max_length':           u'Existe(m) campo(s) que deve(m) ter no máximo %(limit_value)s caracteres.',
    'min_length':           u'Este campo tem que ter no mínimo %(limit_value)s caracteres.',
    'invalid_choice':       u'Existe(m) Opção(ões) inválida(s) selecionada(s).',
    'select_one':           u'Existe(m) item(ns) não selecionado(s).',
}

nagios_messages = {
    'invalid_status':       u'Valor de status incorreto.',
}

sessions_messages = {

        'required':    u'Exite(m) campo(s) não preenchido(s)' ,
        'invalid_choice':       u'Existe(m) Opção(ões) inválida(s) selecionada(s).',
}

help_messages = {

    'invalid_extension' : u'Formato inválido de imagem, os formatos permitidos são JPEG, JPG, PNG e GIF.',
    'invalid_size' : u'Tamanho inválido de imagem, o limite de upload é de 2MBs por imagem.',
    'title_required': u'O campo título é obrigatório.',
    'title_max_length': u'O campo título deve ter no máximo 45 caracteres.',
    'success_upload': u'Upload realizado com sucesso.',
    'invalid_param' : u'Valor da imagem nulo ou inválido.',
}
