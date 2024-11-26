import subprocess
import pandas as pd
import io

def split_ip_port(ip_port_string):
  
  parts = ip_port_string.split('.')
  if len(parts) == 5:
    ip_address = '.'.join(parts[:4])
    port = parts[4]
    return ip_address, port
  else:
    return None


def run_bash_command(command):

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    header=['StartTime', 'Flgs', 'Proto', 'SrcAddr', 'Sport', 'Dir', 'DstAddr', 'Dport', 'TotPkts', 'TotBytes', 'State']
    df=pd.DataFrame(columns=header)
    while True:
        output = process.stdout.readline().decode('utf-8').strip()
        if output == '':
            break
        # print(output.split())
        # new_row=pd.Series(output.split(), index=df.columns)
        # new_df = pd.DataFrame([new_row])
        # df = pd.concat([df, new_df], ignore_index=True)
        print(output)
        

    stderr = process.stderr.read().decode('utf-8').strip()
    if stderr:
        print(f"Error: {stderr}")

    process.wait()

if __name__ == '__main__':
    bash_command = "ra -S localhost:561" 
    run_bash_command(bash_command)