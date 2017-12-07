from invoke import task

image_name = 'gorila:latest'

@task
def build(ctx):
    ctx.run('docker build -t {} .'.format(image_name), pty=True)


@task(pre=[build])
def run(ctx):
    ctx.run('docker run -it {}'.format(image_name), pty=True)


@task
def tdd(ctx):
    test_cmd = 'ptw -p'
    cmd_parts = [
        'docker run -it',
        '-v `pwd`/test:/app/src/test',
        '-w /app/src',
        image_name,
        test_cmd
    ]
    cmd = ' '.join(cmd_parts)
    ctx.run(cmd, pty=True, echo=True)
