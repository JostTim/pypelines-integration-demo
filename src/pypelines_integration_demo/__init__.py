from pypelines import Pipeline, BasePipe, BaseStep


pipeline = Pipeline("demo")


@pipeline.register_pipe
class TextPipe(BasePipe):

    pipe_name = "process_text"

    class HashStep(BaseStep):

        step_name = "get_hashes"

        def worker(self, session, *, extra=None):
            print("hash")

    class VirusCheckStep(BaseStep):

        step_name = "get_virus_check"
        requires = "process_text.get_hashes"

        def worker(self, session, *, extra=None):
            print("virus")
