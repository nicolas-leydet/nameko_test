import time

import click
import eventlet

from nameko.standalone.rpc import ClusterRpcProxy

from nameko_test.settings import AMQP_URI


def call_service(nb_call, delay):
    with ClusterRpcProxy({'AMQP_URI': AMQP_URI}) as proxy:
        start_time = time.perf_counter()

        for _ in range(nb_call):
            proxy.service.answer()
            eventlet.sleep(delay)

        return time.perf_counter() - start_time


@click.command()
@click.option('--calls', default=10, help='Number of calls.')
@click.option('--delay', default=0.0, help='delay between calls')
def run(calls, delay):
    print(call_service(calls, delay))


if __name__ == '__main__':
    run()
