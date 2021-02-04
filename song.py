class Song:
    """
    This :class: creates a song which as the following attributes:
    1. Song name
    2. Artist name
    3. Resource for a song-related image
    4. Song preview URL (if it exists)
    :params:
    
    """
    __attrs__ = [
        'title', 'name', 'thumbnail', 'preview'
    ]
    
    def __init__(self, title, name, thumbnail, preview):
        self.title = title
        self.name = name
        self.thumbnail = thumbnail
        self.preview = preview
    
    def getTitle(self):
        return self.title
        
    def getName(self):
        return self.name
    
    def getThumbnail(self):
        return self.thumbnail
    
    def previewExists(self):
        return not (self.preview is None)
    
    def getPreview(self):
        return self.preview
    
    def getAttrs(self):
        '''
        :return: tuple of title, name, thumbnail, and preview if preview exists
        :rtype: Tuple -> String
        '''
        if self.previewExists():
            return (self.title, self.name, self.thumbnail, self.preview)
        else:
            return (self.title, self.name, self.thumbnail, None)