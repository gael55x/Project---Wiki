# Project - Wiki
A Wikipedia-like website built using the Django Framework. This project aims to create an online encyclopedia where users can access and contribute to various encyclopedia entries.

### Understanding
To understand the project, let's explore some important files and components:

**URL Configuration**: Open the *encyclopedia/urls.py* file. This file defines the URL configuration for the app. You'll notice a default route associated with the views.index function.

**Utility Functions**: Look at *encyclopedia/util.py*. This file contains 4 useful functions for interacting with encyclopedia entries. list_entries returns a list of the names of all saved entries. save_entry saves a new entry with a title and Markdown content. get_entry retrieves an entry by its title, returning its Markdown content if it exists, or None if it doesn't. random_entry returns a random encyclopedia page. These functions can be used in your views. 

**Entry Storage**: Each entry is saved as a Markdown file inside the entries/ directory. Take a look at the existing entries provided. 

**Views**: *Explore encyclopedia/views.py*. The views.py file contains multiple view functions that handle different features of the application. The index(request) function renders the index page by retrieving a list of all entries and passing it to the template. The entry(request, title) function displays individual entry pages, converting the entry's Markdown content to HTML and rendering it with the corresponding title. The search(request) function handles searches, redirecting users to matching entry pages or displaying search results. The new_page(request) function renders the form for creating new encyclopedia entries, while the save_page(request) function handles the saving of new entries. The edit(request, title) function allows users to edit existing entries, updating the content and redirecting to the updated page. The save(request, title) function saves edited content, redirecting to the updated page. Lastly, the random_page(request) function redirects users to a random entry's page.

These view functions collectively handle rendering the index page, displaying individual entries, performing searches, creating new entries, editing existing entries, and redirecting to random entries. They enable the application to provide a user-friendly interface for browsing, creating, and updating encyclopedia entries.

**Templates**: Locate the encyclopedia/templates/encyclopedia/index.html template. This template inherits from layout.html and defines the page's title and body. The body displays an unordered list of all entries. The layout.html file defines the overall structure of the page, including a sidebar with a search field, a home link, and links for creating a new page and visiting a random page (currently non-functional).

### Features
This project includes the following features:

**Entry Page**: Users can access individual encyclopedia entries by visiting /wiki/TITLE, where TITLE represents the desired entry's title. The entry page displays the content of the specific entry. If the requested entry does not exist, an error page is shown.

**Index Page**: The index page lists all available encyclopedia entries. Users can click on an entry name to directly navigate to the corresponding entry page.

**Search**: Users can perform searches by entering a query in the sidebar's search box. If the query matches an existing entry, the user is redirected to that entry's page. If there is no exact match, a search results page is displayed, showing a list of entries containing the query as a substring.

**New Page**: Clicking "Create New Page" in the sidebar takes users to a page where they can create a new encyclopedia entry. They can enter a title and provide the content in Markdown format using a textarea. After saving, the new entry is stored, and the user is redirected to the newly created entry's page. If an entry with the same title already exists, an error message is shown.

**Edit Page**: Each entry page contains a link to edit the entry's content. Clicking this link takes users to an editing page where they can modify the Markdown content of the entry. After saving the changes, users are redirected back to the entry's page.

**Random Page**: Clicking "Random Page" in the sidebar takes users to a randomly selected encyclopedia entry, adding an element of serendipity to the browsing experience.

**Markdown to HTML Conversion**: All Markdown content in the encyclopedia entries is converted to HTML before being displayed to the user. This ensures proper formatting, such as headings, bold text, unordered lists, links, and paragraphs. The conversion is performed using the python-markdown2 package.

By incorporating these features, the Wiki project offers users a comprehensive platform for accessing, searching, creating, and editing encyclopedia entries in a user-friendly and intuitive manner.