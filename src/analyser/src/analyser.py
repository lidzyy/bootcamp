import time
import psutil
import logging
from statistics import mean


#logging para analisar comportamento
logging.basicConfig(
    filename="../logs/output.log",
    level=logging.INFO,
    format="%(asctime)s | CPU: %(message)s"
)

def measure_cpu(interval=1, samples=5):
    """ Mede a %  de cpu em intervalos e devolve media """ 
    values = []
    for _ in range(samples):
        cpu = psutil.cpu_percent(interval = interval)
        values.append(cpu)
        logging.info(f"{cpu}%")
    return mean(values)

def busy_task(n = 50000):
    """ Executa um ciclo artificial so para gerar carga. """
    s = 0
    for i in range(n):
        s += (i * 3) % 7
    return s

if __name__  == "__main__":
    print("Medicao inicial ...")
    base = measure_cpu()
    
    print(f"CPU media ocioca: {base:.1f}%")

    print("A executar carga controlada ...")
    start = time.time()
    busy_task()
    end = time.time()

    used = measure_cpu()
    print(f"CPU media sob carga: {used:.1f}%")
    print(f"Tempo de execucao: {end - start:.3f}s")
    
    logging.info(f"---- run finished in {end - start:.3f}s ----")
