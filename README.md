<h1>Shell Access Bruter</h1>
<img width="1056" height="432" alt="image" src="https://github.com/user-attachments/assets/1c48891c-2249-4f31-975c-263359b04eee" />


<hr>

<h2>Overview</h2>
<p>
This repository contains a simple Python-based login form tester.
The tool is designed for educational purposes and authorized security testing only.
</p>

<p>
It automatically detects password input fields and performs testing using a provided wordlist.
Supports both single target mode and bulk scanning mode.
</p>

<h2>Features</h2>
<ul>
  <li>Single target mode</li>
  <li>Bulk scanning using URL list file</li>
  <li>Automatic password field detection</li>
  <li>Response length comparison (baseline method)</li>
  <li>Redirect & cookie detection</li>
  <li>Lightweight CLI interface</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.9+</li>
  <li>requests</li>
  <li>beautifulsoup4</li>
  <li>colorama</li>
</ul>

<h2>Installation</h2>
<pre>
git clone https://github.com/snapdowgg/Shell-Bruter
cd Shell-Bruter
</pre>

<h2>Usage</h2>
<pre>
python main.py
</pre>

<h3>Single Mode</h3>
<pre>
~$ single
[url]: https://target.com/webshellmasbro.php
[pw]: wordlist.txt
</pre>

<h3>Massive Mode</h3>
<pre>
~$ massive
[url-list]: list.txt
[pw]: wordlist.txt
</pre>

<h2>Output</h2>
<p>
Successful attempts will be saved into:
</p>

<pre>
cracked.txt
</pre>

<h2>How It Works</h2>
<ul>
  <li>Fetch target HTML page</li>
  <li>Automatically detect password field</li>
  <li>Send baseline request with random password</li>
  <li>Compare response length difference</li>
  <li>Detect redirect or set-cookie header</li>
</ul>

<h2>Disclaimer</h2>
<p>
<strong>For educational and authorized security testing purposes only.</strong>
</p>

<p>
The author is not responsible for misuse, illegal activity, or any damage caused by this tool.
Always obtain proper authorization before testing any system.
</p>
