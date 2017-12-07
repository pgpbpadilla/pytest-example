from invoke import task

image_name = 'gorila'

@task
def build(ctx, no_cache=False):
    opts = ''
    if no_cache:
        opts = '--no-cache'
    ctx.run('docker build {} -t {} .'.format(opts, image_name), pty=True)


@task(pre=[build])
def run(ctx):
    ctx.run('docker run -it {}'.format(image_name), pty=True)


@task
def tdd(ctx, cmd=''):
    test_cmd = 'ptw -p -c'
    cmd_parts = [
        'docker run -it',
        '-e PYTHONDONTWRITEBYTECODE=1',  # Don't generate __pychache__
        '-v `pwd`:/app/src',
        '-w /app/src',
        image_name,
        test_cmd if cmd == '' else cmd
    ]
    cmd = ' '.join(cmd_parts)
    ctx.run(cmd, pty=True, echo=True)
