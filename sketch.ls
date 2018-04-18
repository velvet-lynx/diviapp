const SIZE = 75
const WIDTH = 7 * SIZE
const HEIGHT = WIDTH

style = 
  *fill: '#e3a'

line1 = 
    *id: 1,
    name: "Poincare",
    *id: 2,
    name: "Gresilles",
    *id: 3,
    name: "Republique",
    *id: 4,
    name: "Godrans"

line2 = 
    *id: 3,
    name: "Republique",
    *id: 4,
    name: "Godrans"
    *id: 5,
    name: "Darcy"

class Grid 
    (width, height, size) ->
        @grid = @createGrid(width, height, size)


    create-grid: (width, height, size) ->
        grid = []
        for i from 0 to width by size
            temp = []
            for j from 0 to height by size
                temp.push({ x: i, y: j })
            grid.push(temp)
        grid

    get: (col, row) ->
        @grid[col][row]

    get-cell: (colOffset = 0, rowOffset = 0) ->
        parity = @grid.length % 2
        colIndex = Math.round(@grid.length / 2 + colOffset - parity)
        rowIndex = Math.round(@grid[0].length / 2 + rowOffset - parity)
        @get(colIndex, rowIndex)

    test-grid: (draw) ->
        @grid |> map (-> map (point -> draw.circle(10).move(point.x, point.y).attr({ fill: '#000' })))


class Manager
    (lines, grid) ->
        @lines = lines
        @grid = grid

    draw-stop: (position, draw) ->
        draw.rect(20, 20).radius(10).move(position.x-5, position.y-5).attr({ fill: "#000" })

    draw-line: (line, draw, colOffset = 0) ->
        rowOffset = - Math.round(line.length / 2)
        prevPos = @grid.getCell(colOffset, rowOffset) 
        for i from 1 to line.length-1 by 1
            currPos = @grid.getCell(colOffset, rowOffset + i) 
            draw.line(prevPos.x+5, prevPos.y, currPos.x+5, currPos.y).stroke({ color: "#e3a", width: 10})
        for i from 0 to line.length-1 by 1
            position = @grid.getCell(colOffset, rowOffset + i) 
            @drawStop(position, draw)

    draw-lines: (draw) ->
        colOffset = - Math.round(@lines.length / 2)
        for i from 0 to @lines.length-1 by 1
            @drawLine(@lines[i], draw, colOffset + i)

draw = SVG('drawing').size(WIDTH, HEIGHT)

grid = new Grid WIDTH, HEIGHT, SIZE
grid.testGrid(draw)

manager = new Manager [line1, line2, line1], grid 
manager.draw-lines(draw)