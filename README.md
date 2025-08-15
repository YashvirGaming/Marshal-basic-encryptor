<h1>Marshall Basic Encryptor</h1>

<p>
<img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python">
<img src="https://img.shields.io/badge/GUI-CustomTkinter-darkgreen.svg" alt="CustomTkinter">
<img src="https://img.shields.io/badge/Encryption-Marshal-orange.svg" alt="Marshal">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p><strong>Marshall Basic Encryptor</strong> is a dark-themed Python GUI tool that lets you encrypt any <code>.py</code> file using Python's <code>marshal</code> module. The encrypted script can be run directly, helping protect your Python source code from casual inspection.</p>

<h2>✨ Features</h2>
<ul>
<li>Modern <strong>CustomTkinter</strong> dark GUI</li>
<li>One-click <strong>.py</strong> file selection and encryption</li>
<li>Uses Python's <code>marshal</code> for source code compilation &amp; serialization</li>
<li>Auto-generates new <code>_Encrypted.py</code> file ready to execute</li>
<li>Status updates with success message in GUI</li>
<li>Minimal, clean, and beginner-friendly</li>
</ul>

<h2>📦 Installation</h2>
<pre><code>pip install customtkinter
</code></pre>

<h2>🚀 Usage</h2>
<ol>
<li>Run <code>Marshall_Encryptor.py</code></li>
<li>Click <strong>Load &amp; Encrypt .py</strong></li>
<li>Select your Python file</li>
<li>Encrypted file will be saved with <code>_Encrypted.py</code> suffix</li>
</ol>

<h2>🖼 Screenshot</h2>
<p><em><img width="508" height="333" alt="image" src="https://github.com/user-attachments/assets/72a96870-1905-49d6-b03b-6c63d7ad1eb5" /></em></p>

<h2>⚙️ Example Encrypted Output</h2>
<pre><code>import marshal
exec(marshal.loads(b'...'))
</code></pre>

<h2>📜 License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
