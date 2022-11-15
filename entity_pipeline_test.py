from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig # for entity test
from sensor.pipeline import training_pipeline # for pipeline test 
from sensor.pipeline.training_pipeline import TrainPipeline 

if __name__ == '__main__':

    # entity test
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config= DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig())
    print(data_ingestion_config.__dict__)

    # pipeline test
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
