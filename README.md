# Sketchpad Basic

Sketchpad Basic is a lightweight visual communication plugin for ChatGPT. Draw an idea, add a short note, then copy both together to give ChatGPT clear visual context.

## What it does

- Draw with a pen, erase, add text, and place simple shapes
- Preview symbols with an anchor point, size adjustment, and rotation before committing them; Line and Arrow remain direct-drawing tools
- Use bright pink highlights when you want to call attention to an area
- Paste, open, or capture camera images, then move, resize, and rotate them before placing
- Use camera tools such as switch camera, timer, and optional image adjustments
- Add separate Rules for ChatGPT and What to create notes
- Choose quick suggestions for rough concepts, layout, camera references, and pink highlights
- Copy a single image that includes the sketch, notes, and guidance for ChatGPT
- Save your work as a PNG

## Current features

- Select and cut an area, with clipboard protection when copying is unavailable
- Restore a previous sketch after refresh or accidental navigation
- Keyboard shortcuts including Undo, Redo, Escape, and brush-size brackets
- Save PNGs with a clear white background for reliable ChatGPT image interpretation
- Start a New canvas to clear the drawing, notes, pending objects, and view state together
- Live app: [jeremiaharting.github.io/sketchpad-basic](https://jeremiaharting.github.io/sketchpad-basic/)

## Validation

Run the dependency-free smoke tests locally with:

```text
python -m unittest discover -s tests -p "test_*.py" -v
```

The same tests run automatically in GitHub Actions for pushes and pull requests.

## How to use it

1. Open Sketchpad Basic in Codex.
2. Draw, open, paste, or capture an image onto the canvas.
3. Add Rules for ChatGPT to explain how the image should be interpreted.
4. Add What to create to describe the change or result you want.
5. Select **Copy to Chat**, then paste into ChatGPT.

Pink guidance is optional. Select it when pink marks are intentional highlights; otherwise, pink is treated as an ordinary color.

## Plugin files

The installable Codex plugin is in [`sketchpad-basic`](./sketchpad-basic).
