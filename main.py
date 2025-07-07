from src.cli import Cli


def main():
    """Run the Auto Driving Car Simulation"""
    try:
        cli = Cli()
        cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
