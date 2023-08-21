import pygame


class Images:
    def __init__(self):
        self.black_queen = self.load_and_scale(
            'assets/images/b_queen.png', (80, 80))
        self.black_queen_small = self.load_and_scale(
            'assets/images/b_queen.png', (45, 45))

        self.black_king = self.load_and_scale(
            'assets/images/b_king.png', (80, 80))
        self.black_king_small = self.load_and_scale(
            'assets/images/b_king.png', (45, 45))

        self.black_rook = self.load_and_scale(
            'assets/images/b_rook.png', (80, 80))
        self.black_rook_small = self.load_and_scale(
            'assets/images/b_rook.png', (45, 45))

        self.black_bishop = self.load_and_scale(
            'assets/images/b_bishop.png', (80, 80))
        self.black_bishop_small = self.load_and_scale(
            'assets/images/b_bishop.png', (45, 45))

        self.black_knight = self.load_and_scale(
            'assets/images/b_knight.png', (80, 80))
        self.black_knight_small = self.load_and_scale(
            'assets/images/b_knight.png', (45, 45))

        self.black_pawn = self.load_and_scale(
            'assets/images/b_pawn.png', (65, 65))
        self.black_pawn_small = self.load_and_scale(
            'assets/images/b_pawn.png', (45, 45))

        self.white_queen = self.load_and_scale(
            'assets/images/w_queen.png', (80, 80))
        self.white_queen_small = self.load_and_scale(
            'assets/images/w_queen.png', (45, 45))

        self.white_king = self.load_and_scale(
            'assets/images/w_king.png', (80, 80))
        self.white_king_small = self.load_and_scale(
            'assets/images/w_king.png', (45, 45))

        self.white_rook = self.load_and_scale(
            'assets/images/w_rook.png', (80, 80))
        self.white_rook_small = self.load_and_scale(
            'assets/images/w_rook.png', (45, 45))

        self.white_bishop = self.load_and_scale(
            'assets/images/w_bishop.png', (80, 80))
        self.white_bishop_small = self.load_and_scale(
            'assets/images/w_bishop.png', (45, 45))

        self.white_knight = self.load_and_scale(
            'assets/images/w_knight.png', (80, 80))
        self.white_knight_small = self.load_and_scale(
            'assets/images/w_knight.png', (45, 45))

        self.white_pawn = self.load_and_scale(
            'assets/images/w_pawn.png', (65, 65))
        self.white_pawn_small = self.load_and_scale(
            'assets/images/w_pawn.png', (45, 45))

        self.white_images = [self.white_pawn, self.white_queen, self.white_king,
                             self.white_knight, self.white_rook, self.white_bishop]
        self.small_white_images = [self.white_pawn_small, self.white_queen_small, self.white_king_small,
                                   self.white_knight_small, self.white_rook_small, self.white_bishop_small]

        self.black_images = [self.black_pawn, self.black_queen, self.black_king,
                             self.black_knight, self.black_rook, self.black_bishop]
        self.small_black_images = [self.black_pawn_small, self.black_queen_small, self.black_king_small,
                                   self.black_knight_small, self.black_rook_small, self.black_bishop_small]

    def load_and_scale(self, image_path, size):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)
