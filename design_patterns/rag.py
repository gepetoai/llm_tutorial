from voyageai import Client
from dotenv import load_dotenv

load_dotenv()

people = [
    "First name: Alice; Last Name: Johnson; Job Title: DevOps Engineer; Expertise: Terraform, AWS CloudFormation, CI/CD pipelines; Email: alice.johnson@example.com",
    "First name: Bob; Last Name: Smith; Job Title: Machine Learning Engineer; Expertise: TensorFlow, PyTorch, Natural Language Processing; Email: bob.smith@example.com",
    "First name: Carol; Last Name: Williams; Job Title: Frontend Developer; Expertise: React, Vue.js, TypeScript; Email: carol.williams@example.com",
    "First name: David; Last Name: Brown; Job Title: Blockchain Developer; Expertise: Solidity, Ethereum, Smart Contracts; Email: david.brown@example.com",
    "First name: Eve; Last Name: Jones; Job Title: DevOps Engineer; Expertise: AWS, Kubernetes, Docker; Email: eve.jones@example.com",
    "First name: Frank; Last Name: Garcia; Job Title: Embedded Systems Engineer; Expertise: C++, RTOS, ARM Microcontrollers; Email: frank.garcia@example.com",
    "First name: Grace; Last Name: Martinez; Job Title: Data Scientist; Expertise: Python, R, Machine Learning Algorithms; Email: grace.martinez@example.com",
    "First name: Henry; Last Name: Rodriguez; Job Title: Game Developer; Expertise: Unity, C#, 3D Graphics; Email: henry.rodriguez@example.com",
    "First name: Ivy; Last Name: Lee; Job Title: Cybersecurity Analyst; Expertise: Penetration Testing, Threat Modeling, Incident Response; Email: ivy.lee@example.com",
    "First name: Jack; Last Name: Wilson; Job Title: DevOps Engineer; Expertise: AWS, Ansible, Jenkins; Email: jack.wilson@example.com",
    "First name: Karen; Last Name: Taylor; Job Title: Quantum Computing Researcher; Expertise: Quantum Algorithms, Qiskit, Quantum Error Correction; Email: karen.taylor@example.com",
    "First name: Liam; Last Name: Anderson; Job Title: Mobile App Developer; Expertise: Swift, Kotlin, React Native; Email: liam.anderson@example.com",
    "First name: Mia; Last Name: Thomas; Job Title: Robotics Engineer; Expertise: ROS, Computer Vision, Path Planning; Email: mia.thomas@example.com",
    "First name: Noah; Last Name: Jackson; Job Title: Full Stack Developer; Expertise: Node.js, Express, MongoDB; Email: noah.jackson@example.com",
    "First name: Olivia; Last Name: White; Job Title: UX/UI Designer; Expertise: Figma, Adobe XD, User Research; Email: olivia.white@example.com",
    "First name: Peter; Last Name: Harris; Job Title: AR/VR Developer; Expertise: Unity, ARKit, Oculus SDK; Email: peter.harris@example.com",
    "First name: Quinn; Last Name: Martin; Job Title: Bioinformatics Specialist; Expertise: Genomic Data Analysis, BLAST, Python; Email: quinn.martin@example.com",
    "First name: Rachel; Last Name: Thompson; Job Title: IoT Engineer; Expertise: MQTT, LoRaWAN, Embedded C; Email: rachel.thompson@example.com",
    "First name: Samuel; Last Name: Moore; Job Title: Computer Vision Engineer; Expertise: OpenCV, Deep Learning, Image Processing; Email: samuel.moore@example.com",
    "First name: Tara; Last Name: Clark; Job Title: Backend Developer; Expertise: Java, Spring Boot, PostgreSQL; Email: tara.clark@example.com"
]

# Initialize the Voyage AI client
va = Client()

# List to store embedded representations of people
embedded_people = []

# Iterate through each person in the 'people' list
for person in people:
    # Generate an embedding for the person using the 'voyage-3' model
    embedding = va.embed(person, model="voyage-3").embeddings[0]
    
    # Append a tuple of (embedding, person) to the embedded_people list
    embedded_people.append((embedding, person))




import faiss
import numpy as np

# Convert the list of embeddings to a numpy array
embeddings_array = np.array([embedding for embedding, _ in embedded_people], dtype=np.float32)

# Get the dimensionality of the embeddings
dimension = embeddings_array.shape[1]

# Create an in-memory vector database using FAISS
index = faiss.IndexFlatL2(dimension)

# Add the embeddings to the index
index.add(embeddings_array)

def similarity_search(query: str, k: int = 3) -> list[str]:
    # Embed the query string
    query_embedding = va.embed(query).embeddings[0]
    
    # Convert query embedding to numpy array and reshape
    query_array = np.array([query_embedding]).astype('float32')
    
    # Perform the similarity search
    distances, indices = index.search(query_array, k)
    
    # Retrieve the k nearest persons
    nearest_persons = [embedded_people[i][1] for i in indices[0]]
    
    return nearest_persons

# Example usage:
query = "DevOps engineer with expertise in AWS"
results = similarity_search(query, k=3)
print(f"Top 3 matches for '{query}':")

#create k-shot examples to append to the system prompt
k_shot = ""
for person in results:
    k_shot += f"Person: {person}\n"



