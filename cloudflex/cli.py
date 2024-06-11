import click
from cloudflex.commands import init, plan, apply, destroy

@click.group()
def main():
    """CloudFlex CLI"""
    pass

main.add_command(init.init)
main.add_command(plan.plan)
main.add_command(apply.apply)
main.add_command(destroy.destroy)

if __name__ == "__main__":
    main()