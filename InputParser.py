import subprocess

def main():
    process = subprocess.Popen(['sudo', './clicky'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        while True:
            output = process.stdout.readline()
            if output:
                print(output.strip())
            if process.poll() is not None:
                break
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        process.terminate()

if __name__ == "__main__":
    main()
