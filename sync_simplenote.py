from datetime import datetime
from difflib import ndiff
from os.path import exists, getmtime

import simplenote

# https://simplenotepy.readthedocs.io/en/latest/
if __name__ == '__main__':
    # Default the username, but require PW passed as an arg? Lookup in a secure file? OSX keylog?
    sn = simplenote.Simplenote('e@gmail.com', '')
    project_notes = sn.get_note_list(tags=['hugo-sync'])[0]
    for note in project_notes:
        if note['deleted']:
            continue
        project_name = [tag for tag in note['tags'] if tag != 'hugo-sync'][0]
        project_path = f'content/projects/{project_name}.md'
        if not exists(project_path):
            # TODO - create the path and make sure we update from SimpleNote instead of other way
            # around
            pass
        sn_content = note['content']

        hugo_content = ''
        with open(project_path, 'r') as f:
            hugo_content = f.read()
        # print(sn_content)
        # print(hugo_content)

        hugo_mod = datetime.fromtimestamp(getmtime(project_path))
        sn_mod = datetime.fromtimestamp(note['modifydate'])
        print(f'Hugo: {hugo_mod}')
        print(f'SimpleNote: {sn_mod}')
        if sn_mod > hugo_mod:
            print('Updating Hugo from SimpleNote')
            sn_content = sn_content.replace(f'{project_name}\n', '')
            with open(project_path, 'w+') as f:
                f.write(sn_content)
        else:
            print('Updating SimpleNote from Hugo')
            new_note = note
            new_note['content'] = f'{project_name}\n{hugo_content}'
            sn.update_note(new_note)

        # Log the diff just in case a mistake was made
        diff = ndiff(sn_content.splitlines(keepends=True), hugo_content.splitlines(keepends=True))
        diff_rez = [line for line in diff if line.startswith(('-', '+'))]
        print(*diff_rez)

        # TODO
        # - Starting a project on SimpleNote doesn't work as 'w+' auto creates the hugo path and thus
        # the hugo file has a new date
        # - blog posts aren't supported
        # - Even non-changes end up triggering updates and logging everything (metadata file of last
        # time utility was run?)
        # - dry-run flag
        # - log contents of both two two tmp files just in case? (clearing those contents
        # every time we run)
