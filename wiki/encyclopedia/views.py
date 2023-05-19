from django.shortcuts import render, redirect
from django import forms
from . import util
import re
import random

class EditForm(forms.Form):
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={"class": "form-control"}))

def markdown_to_html(markdown):
    # Convert headings
    markdown = re.sub(r'^#\s(.+)$', r'<h1 class="heading">\1</h1><br>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s(.+)$', r'<h2 class="heading">\1</h2><br>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s(.+)$', r'<h3 class="heading">\1</h3><br>', markdown, flags=re.MULTILINE)

    # Convert boldface text
    markdown = re.sub(r'\*\*(.+?)\*\*', r'<strong class="bold">\1</strong><br>', markdown)

    # Convert unordered lists
    markdown = re.sub(r'^\*\s(.+)$', r'<li class="list-item">\1</li><br>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'<li>(.+)</li>', r'<ul><li class="list-item">\1</li></ul><br>', markdown, flags=re.DOTALL)

    # Convert links
    markdown = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" class="link">\1</a><br>', markdown)

    # Convert paragraphs
    paragraphs = re.split(r'\n{2,}', markdown)
    markdown = '<br>'.join(paragraphs)

    # Convert GitHub specific syntax
    markdown = re.sub(r'```css\n(.*?)```', r'<code class="code">\1</code><br>', markdown, flags=re.DOTALL)

    return markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    entry_content = util.get_entry(title)

    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "The requested page was not found."
        })

    # Convert Markdown to HTML
    html_content = markdown_to_html(entry_content)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    query = request.GET.get('q')

    # Check if the query matches an entry exactly
    if util.get_entry(query):
        return redirect('entry', title=query)

    # Check if the query matches any entry partially
    entries = util.list_entries()
    matches = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, 'encyclopedia/search_results.html', {
        'query': query,
        'matches': matches
    })

def new_page(request):
    return render(request, 'encyclopedia/new_page.html')

def save_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Check if an entry with the same title already exists
        if util.get_entry(title):
            return render(request, 'encyclopedia/error.html', {
                'error_message': 'An entry with the same title already exists.'
            })

        # Save the new entry to disk
        util.save_entry(title, content)

        # Redirect the user to the new entry's page
        return redirect('entry', title=title)

    return redirect('index')


def edit(request, title):
    # Retrieve the content of the entry
    content = util.get_entry(title)

    if request.method == "POST":
        # If the request method is POST, process the form data
        form = EditForm(request.POST)
        if form.is_valid():
            # Retrieve the updated content from the form
            updated_content = form.cleaned_data["content"]
            # Save the updated content to the entry
            util.save_entry(title, updated_content)
            # Redirect the user to the updated entry's page
            return redirect("entry", title=title)
    else:
        # If the request method is GET, initialize the form with the entry's content
        form = EditForm(initial={"content": content})

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content,
        "form": form
    })


def save(request, title):
    if request.method == "POST":
        # Process the form data
        form = EditForm(request.POST)
        if form.is_valid():
            # Retrieve the updated content from the form
            updated_content = form.cleaned_data["content"]
            # Save the updated content to the entry
            util.save_entry(title, updated_content)
            # Redirect the user to the updated entry's page
            return redirect("entry", title=title)
    else:
        # If the request method is not POST, redirect the user to the edit page
        return redirect("edit", title=title)


def random_page(request):
    entry_title = util.random_entry()  # Implement the random entry retrieval logic in the `random_entry` function
    return redirect('entry', title=entry_title)