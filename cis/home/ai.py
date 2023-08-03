import chromadb
from chromadb.config import Settings
from langchain import PromptTemplate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="college_db")

collection.add(
    documents=["College of Engineering Kottarakkara has been the leading technical institution in Kerala since it's venture in 2004. CE Kottarakkara offers B.Tech in Computer Science & Engineering (Artificial Intelligence & Machine learning), B.Tech in Computer Science & Engineering and Electronics & Communication Engineering, reflecting the modern technological advancements through its updated syllabus. The College is affiliated to APJ Abdul Kalam Technological University (KTU) and approved by All India Council for Technical Education(AICTE). It is under the management of IHRD(Institute of Human Resources Development)- Established by Govt. of Kerala."],
    metadatas=[{"title":"about college"}],
    ids=["id1"]
)

collection.add(
    documents=["The Labs and Workshops of CEK are well maintained and state of the art ones. They include Computer Lab, Electronics Lab and Electrical Lab. The infrastructure in these labs are adequate enough to prepare the students to deal with modern technologies through regular lab sessions under the supervision of experienced and highly qualified Technical staff and skilled assistants.1.COMPUTER LABThe college provides a well equipped computer lab with high speed internet connectivity.2.Digital Signal Processing LabThe DSP lab deals with the basics of digital signal processing on a digital signal processor. Laboratory courses on hands-on experiments are an integral part of engineering education. The college provides a well equipped Digital Signal Processing lab."],
    metadatas=[{"title":"Labs and Workshops"}],
    ids=["id2"]
)

collection.add(
    documents=["A fully automated modern Library & Information Centre(LIC) is on its way to becoming an outstanding learning resource centre catering to the ever growing and uncompromising information and intellectual requirements of the students, faulty, and researchers .BOOK ISSUed Students - 2 books Faculty - 5 books  Non-teaching staff - 2 books  Period of loan Students - 7 days + (Renewal - 7 days) Faculty - 30 days Non-teaching staff - 10 days Library collections(as on 08/07/2015) Resources	Total No. of volume Books	6937 Journals National - 12 Nos."],
    metadatas=[{"title":"Library"}],
    ids=["id3"]
)

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large") #large x1
#tokenizer = T5Tokenizer.from_pretrained("t5-large")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")



def genrateAnswer(question):
  results = collection.query(
      query_texts=question,
      n_results=1
  )
  context = str(results["documents"])
  # Template
  template="Context = {context} answer the following question based on the context. {question}."

  multiple_input_prompt = PromptTemplate(
      input_variables=["context", "question"],
      template=template
  )
  #formatting
  formatted = multiple_input_prompt.format(context=context, question=question)
  #output
  print(formatted)
  my_text = formatted
  inputs = tokenizer(my_text, return_tensors="pt")
  outputs = model.generate(**inputs, \
                          min_length=20, \
                          max_new_tokens=512, \
                          length_penalty = 2, \
                          num_beams=16, \
                          temperature=0.9, \
                          no_repeat_ngram_size=2, \
                          #num_return_sequences 2,\
                          early_stopping=True)

  output_text_Flan_t5 = tokenizer.batch_decode(outputs, \
                                              skip_special_tokens=True)
  print (output_text_Flan_t5)

# question = "college libriary ?"
# print(genrateAnswer(question))