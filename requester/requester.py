import click
import pkgutil
from jinja2 import Template

@click.command()
@click.option('-u', '--url', default='', help='Web Request URL')
@click.option('-o', '--output', default='./exploit.py', help='Specify path where the generated shall be stored (default ./exploit.py)')
@click.option('-c', '--cookie', default='', multiple=True, help='Add cookie in the format cookie=cookievalue, repeat with --cookie for multiple cookies')
@click.option('--proxy', default='', help='Specify if proxy is present')
@click.option('--noverify', is_flag=True, help='If set, any SSL certificates will be trusted')
@click.option('--filter', default='', help='Specify filter to look for inside response')
@click.option('--wordlist', default='', help='Specify a wordlist for bruteforce attacks')
@click.option('--charlist', is_flag=True, help='Specify if a dictionary of printable characters shall be set up')
@click.option('--verbose', is_flag=True, help='If verbosity is set to True, the script will add output for the response')
def create_file(url, noverify, output, cookie, proxy, filter, wordlist, charlist, verbose):
    template_content = pkgutil.get_data(__name__, "templates/requester.j2").decode()
    template = Template(template_content)
    with open(f'{output}', 'w') as wf:
        wf.write(template.render(
            url=url, cookie=cookie, proxy=proxy, noverify=noverify, filter=filter, wordlist=wordlist, charlist=charlist, verbose=verbose))

if __name__ == '__main__':
    create_file()
