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

    def test_dialogs_trap_tab_focus(self):
        self.assertIn("if (event.key === 'Tab')", APP)
        self.assertIn("event.shiftKey && document.activeElement === first", APP)
        self.assertIn("!element.disabled && element.offsetParent !== null", APP)

    def test_export_handles_high_dpi_and_background_choice(self):
        self.assertIn("const exportScale = canvas.width / Math.max(1, canvas.clientWidth)", APP)
        self.assertIn("const whiteBackground = document.querySelector('#whiteBackground')", APP)
        self.assertIn("saveFile(filename, whiteBackground.checked)", APP)

    def test_recovery_saves_canvas_and_notes(self):
        self.assertIn("localStorage.setItem(recoveryKey", APP)
        self.assertIn("rules: rules.value", APP)
        self.assertIn("note: note.value", APP)
        self.assertIn("setInterval(saveRecovery, 5000)", APP)

    def test_recovery_seeds_undo_history(self):
        self.assertIn("const blank = canvas.toDataURL('image/png')", APP)
        self.assertIn("history = [blank]", APP)
        self.assertIn("redoStack = []", APP)

    def test_object_urls_are_revoked(self):
        self.assertIn("URL.revokeObjectURL(objectUrl)", APP)
        self.assertIn("setTimeout(() => URL.revokeObjectURL(objectUrl), 0)", APP)

    def test_paste_ignores_form_fields(self):
        self.assertIn("event.target.closest('input, textarea, select, [contenteditable=\"true\"]')", APP)

    def test_cut_only_clears_after_clipboard_success(self):
        self.assertIn("snapshot(); ctx.clearRect(selectedArea.x", APP)
        self.assertIn("area was not cut", APP)

    def test_escape_cancels_selection(self):
        self.assertIn("if (selecting || selection)", APP)
        self.assertIn("status.textContent = 'Selection cancelled'", APP)

    def test_clear_requires_confirmation(self):
        self.assertIn("if (history.length && !confirm('Clear the entire sketch?')) return", APP)

    def test_camera_uses_full_frame_without_crop_control(self):
        self.assertNotIn('id="cropCamera"', APP)
        self.assertNotIn('cameraCrop', APP)
        self.assertIn("snapshotCtx.drawImage(cameraPreview, -sourceW / 2, -sourceH / 2, sourceW, sourceH)", APP)

    def test_camera_controls_use_clear_labels(self):
        self.assertIn('id="toggleCameraAdjustments"', APP)
        self.assertIn('>Adjust image</button>', APP)
        self.assertIn('>Capture photo</button>', APP)
        self.assertIn('>Saturation <input id="cameraSaturation"', APP)
        self.assertIn("Hide adjustments", APP)

    def test_camera_dialog_owns_camera_layout_class(self):
        self.assertIn('id="cameraDialog" class="dialog-backdrop"', APP)
        self.assertIn('class="dialog choice-dialog camera-dialog" role="dialog" aria-modal="true" aria-labelledby="cameraTitle"', APP)
        self.assertIn('class="dialog choice-dialog" role="dialog" aria-modal="true" aria-labelledby="imageTitle"', APP)

    def test_pasted_images_are_anchored_and_cut_size_is_preserved(self):
        self.assertIn("lastCutSize = { w: selectedArea.w, h: selectedArea.h }", APP)
        self.assertIn("const naturalSize = lastCutSize", APP)
        self.assertIn("naturalSize, point: { x: canvas.clientWidth / 2, y: canvas.clientHeight / 2 }, size: null, scale: 1, rotation: 0, anchored: true", APP)
        self.assertIn("pendingImage.naturalSize ? 1", APP)

    def test_placement_controls_exist(self):
        self.assertIn('id="placeObject"', APP)
        self.assertIn('id="cancelObject"', APP)
        self.assertIn("commitPendingImage()", APP)
        self.assertIn("commitPendingShape()", APP)


if __name__ == "__main__":
    unittest.main()
