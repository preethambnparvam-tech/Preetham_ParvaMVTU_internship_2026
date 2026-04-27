import os

filepath = r'c:\Users\Preet\OneDrive\Desktop\Preetham_ParvaMVTU_internship_2026\Backend\Django\myproject\product_management_app\templates\product-management_app\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = ['{% load static %}\n'] + lines[:35] + ['    <script type="text/babel" src="{% static \'product_management_app/js/app.js\' %}"></script>\n'] + lines[240:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Updated index.html successfully.')
