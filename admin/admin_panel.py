"""
Admin Panel - View all users and games
"""

import pygame as p
from database.db import Database
from typing import Optional

class AdminPanel:
    """Admin panel for viewing all users and games"""
    
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.screen = p.display.set_mode((width, height))
        p.display.set_caption("Chess Admin Panel")
        
        # Colors (emerald theme)
        self.BG_COLOR = (40, 44, 52)
        self.PANEL_COLOR = (50, 54, 62)
        self.HEADER_COLOR = (16, 185, 129)
        self.TEXT_COLOR = (255, 255, 255)
        self.TEXT_GRAY = (158, 158, 158)
        self.HIGHLIGHT_COLOR = (70, 74, 82)
        self.BUTTON_COLOR = (16, 185, 129)
        self.BUTTON_HOVER = (52, 211, 153)
        self.BUTTON_DANGER = (244, 67, 54)
        
        # Fonts
        self.title_font = p.font.SysFont("Arial", 36, bold=True)
        self.header_font = p.font.SysFont("Arial", 24, bold=True)
        self.font = p.font.SysFont("Arial", 18)
        self.small_font = p.font.SysFont("Arial", 14)
        
        # State
        self.view_mode = "users"  # 'users' or 'games'
        self.scroll_offset = 0
        self.max_scroll = 0
        
        # Database
        self.db = Database()
        
        # Data
        self.users = []
        self.games = []
        self.load_data()
        
        # UI elements
        self.back_button_rect = None
        self.users_tab_rect = None
        self.games_tab_rect = None
        
        self.clock = p.time.Clock()
    
    def load_data(self):
        """Load users and games from database"""
        self.users = self.db.get_all_users()
        self.games = self.db.get_all_games(limit=100)
        print(f"Admin: Loaded {len(self.users)} users, {len(self.games)} games")
    
    def draw_button(self, x, y, width, height, text, color=None, hover_color=None):
        """Draw a button"""
        if color is None:
            color = self.BUTTON_COLOR
        if hover_color is None:
            hover_color = self.BUTTON_HOVER
        
        mouse_pos = p.mouse.get_pos()
        rect = p.Rect(x, y, width, height)
        is_hover = rect.collidepoint(mouse_pos)
        
        p.draw.rect(self.screen, hover_color if is_hover else color, rect, border_radius=6)
        
        text_surf = self.font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)
        
        return rect
    
    def draw_tab(self, x, y, width, height, text, active):
        """Draw a tab button"""
        mouse_pos = p.mouse.get_pos()
        rect = p.Rect(x, y, width, height)
        is_hover = rect.collidepoint(mouse_pos)
        
        if active:
            color = self.BUTTON_COLOR
        elif is_hover:
            color = self.BUTTON_HOVER
        else:
            color = self.PANEL_COLOR
        
        p.draw.rect(self.screen, color, rect, border_radius=6)
        
        text_surf = self.header_font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)
        
        return rect
    
    def draw_users_view(self):
        """Draw users table"""
        start_y = 180
        row_height = 60
        
        # Table header
        header_rect = p.Rect(40, start_y, self.width - 80, 50)
        p.draw.rect(self.screen, self.HEADER_COLOR, header_rect, border_radius=8)
        
        # Column headers
        headers = ["ID", "Username", "Email", "Created", "Last Login"]
        col_widths = [60, 150, 220, 150, 150]
        x_pos = 50
        
        for header, width in zip(headers, col_widths):
            text = self.font.render(header, True, self.TEXT_COLOR)
            self.screen.blit(text, (x_pos, start_y + 15))
            x_pos += width
        
        # User rows
        y_pos = start_y + 60
        
        for i, user in enumerate(self.users):
            if y_pos > self.height - 100:
                break
            
            # Alternating row colors
            row_rect = p.Rect(40, y_pos, self.width - 80, row_height)
            if i % 2 == 0:
                p.draw.rect(self.screen, self.PANEL_COLOR, row_rect, border_radius=6)
            
            # User data
            x_pos = 50
            
            # ID
            text = self.small_font.render(str(user['user_id']), True, self.TEXT_COLOR)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[0]
            
            # Username
            text = self.font.render(user['username'], True, self.TEXT_COLOR)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[1]
            
            # Email
            text = self.small_font.render(user['email'], True, self.TEXT_GRAY)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[2]
            
            # Created date
            created = user['created_at'].split()[0] if user['created_at'] else "N/A"
            text = self.small_font.render(created, True, self.TEXT_GRAY)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[3]
            
            # Last login
            last_login = user['last_login'].split()[0] if user['last_login'] else "Never"
            text = self.small_font.render(last_login, True, self.TEXT_GRAY)
            self.screen.blit(text, (x_pos, y_pos + 20))
            
            y_pos += row_height
    
    def draw_games_view(self):
        """Draw games table"""
        start_y = 180
        row_height = 60
        
        # Table header
        header_rect = p.Rect(40, start_y, self.width - 80, 50)
        p.draw.rect(self.screen, self.HEADER_COLOR, header_rect, border_radius=8)
        
        # Column headers
        headers = ["ID", "Player", "Difficulty", "Result", "Moves", "Date"]
        col_widths = [60, 150, 120, 100, 80, 150]
        x_pos = 50
        
        for header, width in zip(headers, col_widths):
            text = self.font.render(header, True, self.TEXT_COLOR)
            self.screen.blit(text, (x_pos, start_y + 15))
            x_pos += width
        
        # Game rows
        y_pos = start_y + 60
        
        for i, game in enumerate(self.games):
            if y_pos > self.height - 100:
                break
            
            # Alternating row colors
            row_rect = p.Rect(40, y_pos, self.width - 80, row_height)
            if i % 2 == 0:
                p.draw.rect(self.screen, self.PANEL_COLOR, row_rect, border_radius=6)
            
            # Game data
            x_pos = 50
            
            # ID
            text = self.small_font.render(str(game['game_id']), True, self.TEXT_COLOR)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[0]
            
            # Username
            text = self.font.render(game['username'], True, self.TEXT_COLOR)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[1]
            
            # Difficulty
            diff_color = {
                'easy': (76, 175, 80),
                'medium': (255, 152, 0),
                'hard': (244, 67, 54)
            }.get(game['difficulty'], self.TEXT_COLOR)
            text = self.font.render(game['difficulty'].capitalize(), True, diff_color)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[2]
            
            # Result
            result = game['result'] or 'ongoing'
            result_color = {
                'win': (76, 175, 80),
                'loss': (244, 67, 54),
                'draw': (255, 152, 0),
                'resign': (158, 158, 158)
            }.get(result, self.TEXT_GRAY)
            text = self.font.render(result.capitalize(), True, result_color)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[3]
            
            # Moves
            text = self.small_font.render(str(game['total_moves']), True, self.TEXT_GRAY)
            self.screen.blit(text, (x_pos, y_pos + 20))
            x_pos += col_widths[4]
            
            # Date
            date = game['started_at'].split()[0] if game['started_at'] else "N/A"
            text = self.small_font.render(date, True, self.TEXT_GRAY)
            self.screen.blit(text, (x_pos, y_pos + 20))
            
            y_pos += row_height
    
    def draw(self):
        """Draw the admin panel"""
        self.screen.fill(self.BG_COLOR)
        
        # Title
        title = self.title_font.render("🛡️ Admin Panel", True, self.HEADER_COLOR)
        self.screen.blit(title, (40, 30))
        
        # Stats summary
        total_users = len(self.users)
        total_games = len(self.games)
        stats_text = f"{total_users} Users  •  {total_games} Games"
        stats = self.font.render(stats_text, True, self.TEXT_GRAY)
        self.screen.blit(stats, (40, 80))
        
        # Tabs
        tab_y = 120
        self.users_tab_rect = self.draw_tab(40, tab_y, 150, 45, "Users", self.view_mode == "users")
        self.games_tab_rect = self.draw_tab(200, tab_y, 150, 45, "Games", self.view_mode == "games")
        
        # Content
        if self.view_mode == "users":
            self.draw_users_view()
        else:
            self.draw_games_view()
        
        # Back button
        self.back_button_rect = self.draw_button(
            self.width - 140, self.height - 60, 120, 45, "Back"
        )
        
        p.display.flip()
    
    def handle_click(self, pos):
        """Handle mouse clicks"""
        if self.users_tab_rect and self.users_tab_rect.collidepoint(pos):
            self.view_mode = "users"
        elif self.games_tab_rect and self.games_tab_rect.collidepoint(pos):
            self.view_mode = "games"
        elif self.back_button_rect and self.back_button_rect.collidepoint(pos):
            return False  # Exit admin panel
        return True
    
    def run(self):
        """Run the admin panel"""
        running = True
        
        while running:
            self.clock.tick(60)
            
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
                    return False
                
                elif event.type == p.MOUSEBUTTONDOWN:
                    running = self.handle_click(event.pos)
            
            self.draw()
        
        return True
    
    def close(self):
        """Close admin panel"""
        self.db.close()


# Test
if __name__ == "__main__":
    p.init()
    admin = AdminPanel()
    admin.run()
    admin.close()
    p.quit()