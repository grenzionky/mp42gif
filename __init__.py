from anki import models
from anki.hooks import addHook
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import re, subprocess
<<<<<<< HEAD
from . import ffmpeg
=======
#import ffmpeg
>>>>>>> main

def setupMenu(browser):
  def mp42gif(browser):
    notes = browser.selectedNotes()
    if notes and len(browser.selectedCards()) > 1:
      count = 0
      note_count = 0

      # set up progress bar
      progress = QProgressDialog("Converting mp4s to gifs...", "", 0, len(notes))
      progress.setWindowModality(Qt.WindowModal)
      progress.setCancelButton(None)

      for nid in notes:
        note = mw.col.getNote(nid)
        fields = mw.col.models.fieldNames(note.model())
        for field in fields:
          # now convert the actual mp4 into a gif
<<<<<<< HEAD
          for name in re.findall(r'\[sound:(.*?)\.ogv\]', note[field]):
            mp4 = re.sub(r"(?i)\.(anki2)$", ".media", mw.col.path)+"/"+name
            ffmpeg.input(mp4+".ogv").video.filter("scale", 480, -1).output(mp4+".gif", framerate=30).overwrite_output().run_async()
            # subprocess.run(["ffmpeg","-i",mp4+".ogv","-r","30","-vf","scale=480:-1",mp4+".gif","-y"])

          # edit html of any field with a mp4 video into gif format
          oldnote = note[field]
          note[field] = re.sub(r'\[sound:(.*?)\.ogv\]', r'<img src="\1.gif" />', note[field])
=======
          for name in re.findall(r'\[sound:(.*?)\.mp4\]', note[field]):
            mp4 = re.sub(r"(?i)\.(anki2)$", ".media", mw.col.path)+"/"+name
            # ffmpeg.input(mp4+".mp4").video.filter("scale", 480, -1).output(mp4+".gif", framerate=30).overwrite_output().run_async()
            subprocess.run(["ffmpeg","-i",mp4+".mp4","-r","30","-vf","scale=480:-1",mp4+".gif","-y"])

          # edit html of any field with a mp4 video into gif format
          oldnote = note[field]
          note[field] = re.sub(r'\[sound:(.*?)\.mp4\]', r'<img src="\1.gif" />', note[field])
>>>>>>> main
          if note[field] != oldnote: count += 1
        note.flush()

        # update progress bar
        note_count += 1
        progress.setValue(note_count)

      showInfo('Done converting '+str(count)+' videos in '+str(len(notes))+' notes.'+'\n\nDon\'t forget to press "Tools>Check Media" to remove the mp4 videos that you aren\'t using anymore.\n')
    else:
      showInfo('Please select the cards you want to convert.\nIf you have a card selected already, then try selecting two or more cards then try again.')
    
  action = QAction('mp42gif', browser)
  action.triggered.connect(lambda: mp42gif(browser))
  browser.form.menuEdit.addSeparator()
  browser.form.menuEdit.addAction(action)
  browser.form.menuEdit.addSeparator()

addHook("browser.setupMenus", setupMenu)
