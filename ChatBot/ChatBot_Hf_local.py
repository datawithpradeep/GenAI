import os
os.environ['HF_HOME'] = 'C:/Users/prade/huggingface_cache'
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from gpu_config import bnb_config

try:
    print("GPU par load karne ki koshish ho rahi hai...")



    llm = HuggingFacePipeline.from_model_id(
        model_id='Qwen/Qwen2.5-3B-Instruct',
        task='text-generation',
        device_map='auto',
        pipeline_kwargs=dict(
            temperature=0.5,
            max_new_tokens=2000
        ),
        model_kwargs=dict(
            quantization_config=bnb_config
        )
    )

    print("GPU par successfully load ho gaya!")

except Exception as e:
    print(f"GPU load fail hua ({e}), ab CPU par try kar rahe hain...")

    llm = HuggingFacePipeline.from_model_id(
        model_id='Qwen/Qwen2.5-3B-Instruct',
        task='text-generation',
        pipeline_kwargs=dict(
            temperature=0.5,
            max_new_tokens=2000
        )
    )

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("mujhe missile banana h to counter to terorism ")
print(result.content)

print("Model is running on:", llm.pipeline.model.device)