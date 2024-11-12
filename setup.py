class TestSetup:
    def __init__(self, app_path):
        self.app_path = app_path
    
    def register_aut(self):
        print(f"Registering AUT at {self.app_path}")
    
    def configure_settings(self):
        print("Configuring test settings")
    
    def setup(self):
        self.register_aut()
        self.configure_settings()

if __name__ == "__main__":
    test_setup = TestSetup('/path/to/your/app')
    test_setup.setup()
