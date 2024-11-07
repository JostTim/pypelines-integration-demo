from pypelines import Pipeline, BasePipe, BaseStep


pipeline = Pipeline("demo")


@pipeline.register_pipe
class TextPipe(BasePipe):

    pipe_name = "process_text"

    class HashStep(BaseStep):

        step_name = "get_hashes"
