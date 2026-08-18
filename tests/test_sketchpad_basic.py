from pathlib import Path
import unittest


APP = (Path(__file__).parents[1] / "sketchpad-basic" / "index.html").read_text(encoding="utf-8")


class SketchpadSmokeTests(unittest.TestCase):
    def test_required_canvas_controls_exist(self):
        for control in ("canvas", "preview", "undo", "redo", "selectTool", "cut", "save", "send"):
            self.assertIn(f'id="{control}"', APP)

    def test_eraser_uses_transparent_compositing(self):
        self.assertIn("globalCompositeOperation = tool === 'eraser' ? 'destination-out' : 'source-over'", APP)

    def test_undo_and_redo_are_wired(self):
        self.assertIn("redoStack.push(canvas.toDataURL())", APP)
        self.assertIn("restore(history.pop())", APP)
        self.assertIn("history.push(canvas.toDataURL())", APP)
        self.assertIn("restore(redoStack.pop())", APP)

    def test_selection_and_cut_are_wired(self):
        self.assertIn("function cutSelection()", APP)
        self.assertIn("selection = null", APP)
        self.assertIn("document.querySelector('#cut').onclick = cutSelection", APP)

    def test_switching_tools_exits_selection_mode(self):
        self.assertIn("function setTool(next) { selecting = false", APP)
        self.assertIn("document.querySelector('#selectTool').classList.remove('active')", APP)

    def test_export_handles_high_dpi_and_background_choice(self):
        self.assertIn("const exportScale = canvas.width / Math.max(1, canvas.clientWidth)", APP)
        self.assertIn("const whiteBackground = document.querySelector('#whiteBackground')", APP)
        self.assertIn("saveFile(filename, whiteBackground.checked)", APP)

    def test_recovery_saves_canvas_and_notes(self):
        self.assertIn("localStorage.setItem(recoveryKey", APP)
        self.assertIn("rules: rules.value", APP)
        self.assertIn("note: note.value", APP)
        self.assertIn("setInterval(saveRecovery, 5000)", APP)

    def test_placement_controls_exist(self):
        self.assertIn('id="placeObject"', APP)
        self.assertIn('id="cancelObject"', APP)
        self.assertIn("commitPendingImage()", APP)
        self.assertIn("commitPendingShape()", APP)


if __name__ == "__main__":
    unittest.main()
