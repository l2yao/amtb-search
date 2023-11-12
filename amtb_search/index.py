from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(input_dir="../amtb/doc/認識佛教", recursive=True).load_data()
index = VectorStoreIndex.from_documents(documents)