import streamlit as st
import functions

todo_list = functions.read_todo_list()

st.set_page_config(layout='wide')


def add_task():
    new_task = st.session_state['new_task']
    new_task = new_task.strip('\n')
    if len(new_task) > 0:
        todo_list.append(new_task + '\n')
        functions.write_todo_list(todo_list)
        st.session_state['new_task'] = ''


st.title("To-Do List")
st.header("This is my To-Do App")
st.write("Check the box when you have <b>completed</b> your task!",
         unsafe_allow_html=True)

for index, task in enumerate(todo_list):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_list(todo_list)
        del st.session_state[task]
        st.experimental_rerun()
        print(checkbox)

st.text_input(label='', placeholder='Enter your task...', key='new_task', on_change=add_task)
