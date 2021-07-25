from github import Github, InputFileContent
class Gist():
    """
    Gist manager that handle the update and the read of a GitHub gist.
    `get` and `create` static method are used to retrieve or create a Gist.
    """

    @staticmethod 
    def get(user, file_name):
        gist = None
        for gs in user.get_gists():
            if file_name in gs.files.keys():
                gist = gs
        return Gist(gist, file_name)

    @staticmethod
    def create(user, file_name, content, description, public=False):
        user.create_gist(
            public=public, 
            files={file_name: InputFileContent(content)}, 
            description=description)
        return Gist.get(user, file_name)

    def __init__(self, gist, file_name):
        self.gist = gist
        self.file_name = file_name
    
    def update(self, new_content):
        self.gist.edit(files = {self.file_name : InputFileContent(new_content)})

    def get_content(self):
        return self.gist.files[self.file_name].content
