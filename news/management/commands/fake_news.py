import djclick as click
from datetime import date, timedelta
from news.models import Article


@click.command()
def command():

    today = date.today()

    for i, title in enumerate(
        [
            "You Won’t Believe What This Developer Found in Their Old Codebase (Hint: It’s Not Just Shame)",
            "Local Man Achieves Inbox Zero, Ascends to Higher Plane of Existence",
            "This One Weird Trick Will Make Your Boss Think You’re Working",
            "10 Signs You’re a Senior Developer (#7 Is Just Screaming Into the Void)",
        ]
    ):

        Article.objects.get_or_create(
            title=title, date=today - timedelta(days=i), defaults={"content": content}
        )


content = """
# Lorem Ipsum Dolor Sit Amet

<c-youtube title="The title" caption="the caption" video_id="rbNuWi7GjKI"/>

## Introduction

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.  
Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris.  
Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla.

## Section One: Sed Dignissim

Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh.  
Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem.  
Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa.  
Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum.

### Subsection: Nulla Malesuada

Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit.  
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

- Etiam porta sem malesuada magna mollis euismod.  
- Cras justo odio, dapibus ac facilisis in, egestas eget quam.  
- Donec ullamcorper nulla non metus auctor fringilla.

## Section Two: Integer Posuere

Vestibulum id ligula porta felis euismod semper. Cras justo odio, dapibus ac facilisis in, egestas eget quam.  
Curabitur blandit tempus porttitor. Nullam quis risus eget urna mollis ornare vel eu leo.  
Integer posuere erat a ante venenatis dapibus posuere velit aliquet.

```bash
# Sample code block
echo "Lorem ipsum dolor sit amet"
```
"""
