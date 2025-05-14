<div align="center">
  <h1>🤖 RecruitX</h1>
  <p>AI-Powered Recruitment Automation System</p>

  <div>
    <img src="https://img.shields.io/badge/Version-1.0.0-blue" alt="Version">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/Python-3.10%2B-yellow" alt="Python">
  </div>
</div>

<h2>📌 Table of Contents</h2>
<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#agents">Agent Architecture</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="overview">🚀 Overview</h2>
<p>RecruitX revolutionizes hiring through AI agents that handle:</p>
<ul>
  <li>✅ Job Description Generation</li>
  <li>📄 Resume Screening & Scoring</li>
  <li>🎯 Interview Automation</li>
  <li>🤖 AI-Powered Decision Making</li>
</ul>

<h2 id="features">✨ Key Features</h2>
<table>
  <tr>
    <th>Module</th>
    <th>Capabilities</th>
  </tr>
  <tr>
    <td>JD Builder</td>
    <td>AI-generated job descriptions with 10+ templates</td>
  </tr>
  <tr>
    <td>Resume Parser</td>
    <td>PDF/DOCX parsing with 95% accuracy</td>
  </tr>
  <tr>
    <td>AI Screening</td>
    <td>Semantic matching using Sentence-BERT</td>
  </tr>
  <tr>
    <td>Interview Agent</td>
    <td>Auto-generated questions & transcript analysis</td>
  </tr>
</table>

<h2 id="installation">⚙️ Installation</h2>
<pre><code># Clone repository
git clone https://github.com/MdAzhar5/RecruitX.git

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
</code></pre>

<h2 id="usage">📋 Basic Usage</h2>
<h3>1. Create Job Description</h3>
<pre><code>python recruitx.py jd create --role "Senior Developer"</code></pre>

<h3>2. Process Applicants</h3>
<pre><code>python recruitx.py process --jd senior_dev.yaml --resumes ./resumes/</code></pre>

<h2 id="agents">🤖 Agent Architecture</h2>
<div align="center">
</div>

<h3>Core Agents</h3>
<ul>
  <li><strong>JD Builder Agent</strong>: Creates job descriptions</li>
  <li><strong>Resume Parser Agent</strong>: Extracts candidate data</li>
  <li><strong>Scoring Agent</strong>: Matches resumes to JDs</li>
  <li><strong>Interview Agent</strong>: Manages Q&A analysis</li>
</ul>

<h2 id="contributing">👥 Contributing</h2>
<ol>
  <li>Fork the repository</li>
  <li>Create your feature branch (<code>git checkout -b feature/amazing</code>)</li>
  <li>Commit changes (<code>git commit -m 'Add amazing feature'</code>)</li>
  <li>Push to branch (<code>git push origin feature/amazing</code>)</li>
  <li>Open a Pull Request</li>
</ol>

<h2 id="license">📜 License</h2>
<p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>

<div align="center">
  <p>💬 Contact: <a href="mailto:support@recruitx.ai">support@recruitx.ai</a></p>
</div>
