import time

import click

from nameko.standalone.rpc import ClusterRpcProxy

from nameko_test.settings import AMQP_URI
from kombu import Exchange


Exchange.delivery_mode = 1

NB_TESTS = 10


def call_service(nb_call):
    with ClusterRpcProxy({'AMQP_URI': AMQP_URI}) as proxy:
        start_time = time.perf_counter()

        calls = [proxy.service.answer.async() for _ in range(nb_call)]

        dt = time.perf_counter() - start_time

        [call.result() for call in calls]

        dt_after_join = time.perf_counter() - start_time

        return dt, dt_after_join


@click.command()
@click.option('--calls', default=10, help='Number of calls.')
def run(calls):

    tests = (call_service(calls) for _ in range(NB_TESTS))

    elapsed_times = [dts for dts in tests]
    elapsed_times = list(zip(*elapsed_times))
    cps = sum(float(calls) / dt
              for dt in elapsed_times[0]) / NB_TESTS
    cps_after_join = sum(float(calls) / dt
                         for dt in elapsed_times[1]) / NB_TESTS

    print(f'calls only: {cps} calls per second')
    print(f'after result: {cps_after_join} calls per second')

if __name__ == '__main__':
    run()
