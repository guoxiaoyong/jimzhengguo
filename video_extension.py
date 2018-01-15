import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

tmpl = """
<div style="border: 5px yellow solid; padding:5px">
<video class="video-js" controls preload="auto" width="800" height="600"
  poster="images/poster.png" data-setup="{{}}"
  style="border: 2px green solid"
>
    <source src="{video_src}" type='video/mp4'>
</video>
</div>
""".replace('\n', '')

pattern = r'\[\[video:[\a-z0-9_.]+\]\]'
baseurl = 'https://guoxiaoyong.github.io/homework_kangaroo/'
class VideoPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.findall(pattern, line)
            if m:
               video_src = baseurl + m[0][8:-2]
               line = tmpl.format(video_src=video_src)
               new_lines.append(line+'\n')
            else:
                new_lines.append(line)
        return new_lines


class VideoExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        # Insert instance of 'mypattern' before 'references' pattern
        md.preprocessors.add('video_preprocessor', VideoPreprocessor(md), '_end')
