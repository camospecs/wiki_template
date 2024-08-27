# Setting up the wiki.

1. Clone using:

    ```bash
    git clone   https://github.com/camospecs/wiki_template
    ```

2. Setup virtual environment.

    ```bash
    sudo apt update && sudo apt upgrade -y #Normal housekeeping 
    sudo apt install python3-virtualenv -y

    cd wiki_template
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

    ```

3. Initialising the post database.

```bash
cd instance
python3 post_builder.py
# Follow prompts to make first post.

```

4. Start the web application

```bash
sudo python3 app.py
```

5. Navigate to http://127.0.0.1:5000

# Creating a post.

1. Once the db has been initialised, you can use post_builder to make posts.

```bash
cd ~/wiki_template/instance
python3 post_buidler.py
```

2. Here is an example of a post being built.

```
DB Post Builder.
Title: Cloudflare DNS
Brief: This a guide on how to use cloudflare DNS.
HTML: <p> Here is some example code</p> <pre><code>printf("Hello World!");</code></pre>
Image path: static/images/cloudflare.webp
```

