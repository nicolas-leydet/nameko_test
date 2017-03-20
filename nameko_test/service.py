import click

import eventlet

from nameko.rpc import rpc
from nameko.dependency_providers import Config
from nameko.cli.run import run as nameko_run

from nameko_test.settings import AMQP_URI


class Service(object):
    name = 'service'

    config = Config()

    @property
    def delay(self):
        return self.config.get('delay', 0)

    @rpc
    def answer(self):
        eventlet.sleep(self.delay)
        return 42


@click.command()
@click.option('--workers', default=10, help='Number of workers.')
@click.option('--delay', default=0.0, help='Method delay')
def run(workers, delay):
    nameko_run([Service],
               config={
                   'AMQP_URI': AMQP_URI,
                   'max_workers': workers,
                   'delay': delay,
               })


if __name__ == '__main__':
    run()
