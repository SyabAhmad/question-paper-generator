import streamlit as st
import time
import backend.generate as generatesRespose

st.header("Paper Generator App")
st.markdown("""
            
Hello and welcome to the Paper Generator App! This application helps you generate papers for various subjects based on your specified criteria. Whether you are a student looking for practice papers or an educator creating assessments, this tool has got you covered.

## Instructions on How to Use

1. **Book Name:** Enter the name of the book related to the subject.

2. **Class:** Specify the class or semester for which you want to generate the paper.

3. **Chapter Name:** Enter the name of the chapter or topic for the paper.

4. **Advanced or Basic:** Choose the difficulty level, whether advanced or basic.

### Example Usage

For example, to generate a paper for Software Engineering in the 7th semester, focusing on the UML chapter with basic difficulty:

- **Book Name:** Software Engineering
- **Class:** 7 Semester
- **Chapter Name:** UML
- **Advanced or Basic:** Basic

### Select Paper Type

Choose the type of paper you want to generate:
            
            """)


bookName = ''
classs = ''
chapterName = ''
levelOfPaper = ''
extraDetails = ''
paperType = ''

def MainFunction(inputMessage):
    inputMessageList = []

    inputMessageList = inputMessage.split(',')
    
    bookName = inputMessageList[0]
    classs = inputMessageList[1]
    chapterName = inputMessageList[2]
    levelOfPaper = inputMessageList[3]

    
    # st.selectbox("Select Paper Type", ['Long Questions','Short Questions','MCQs','Blanks','TRUE or FALSE'])
    # text = generatesRespose.generate(bookName, classs,chapterName, levelOfPaper, paperType)
    # patter = f'Generate a paper for class {classs}, the name of the book is {bookName} and the chapter name is {chapterName}, and should be {levelOfPaper}'
    
    
    col1, col2 = st.columns([1,10])
    with col1:  
        st.success(f'👨')
    with col2:
        time.sleep(.2)
        st.success(f'Book: {bookName}')
        time.sleep(.2)
        st.success(f'Chapter Name: {chapterName}')
        time.sleep(.2)
        st.success(f'Class Name: {classs}')
        time.sleep(.2)
        st.success(f'Level: {levelOfPaper}')
    with st.spinner("Loading model ..."):
        text = generatesRespose.generate(bookName, classs,chapterName, levelOfPaper,paperType)
        index = 0
        with open("data.txt", "a") as file:
            file.write(f'[{index}:{text}]\n\n')
            index += 1
        
        
        textSize = len(text)
        col1, col2 = st.columns([1,10])
        with col1:  
            st.success(f'👨‍💻')
        with col2:
            st.success(f'{text}')
            col1, col2 = st.columns([8,4])
            with col1:
                st.code(f'Total Words Generated: {textSize}')
            with col2:
                pass
                # copyButton = st.button("Copy: Not Working yet",on_click=st.balloons)
                

inputMessage = st.text_input("book name, class, chapter name, advance or basic")
paperType = st.selectbox("Select Paper Type", ['Long Questions','Short Questions','MCQs','Blanks','TRUE or FALSE'])

button = st.button("Generate")
if button:
    MainFunction(inputMessage)
    


