from site_setup.models import SiteSetup


def context_processor_exemple(request):
    return {
        'example': 'teste çlksjdçf'
    }


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    # print(setup.query)  --- consultar a query de consulta do banco de dados

    return {
        'site_setup': setup
    }
