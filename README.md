<h1 style="margin: 0">2021F-CPE-551-WS-Final-Project</h1>

<a href="https://youtu.be/qNsNCAhYNps" style="display: block; margin: 10px 0; font-size: 18px">
See it in action on YouTube
</a>

<p>
This is a python script that accepts a Github API token and a Github username as command line arguments. The script then uses Github APIs to find all the repos belonging to the provided user and star them.
</p>

<p>
Two different Github APIs are used in the script.
</p>

<code style="display: block; margin: 10px 0">
repos_endpoint = 'https://api.github.com/users/%s/repos' % github_username
</code>
<p>and</p>
<code style="display: block; margin: 10px 0">
star_endpoint = 'https://api.github.com/user/starred/%s/%s' % (github_username, repo['name'])
</code>
<p>
The script uses the requests library to send HTTP requests and the sys library to read command line arguments.
</p>