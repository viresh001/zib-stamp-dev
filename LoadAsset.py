
class LoadAsset():

    def load_asset(self,f):
        with open(f, 'rb', buffering=0) as input:
            data = input.read()

        assert isinstance(data, bytes)

        return data