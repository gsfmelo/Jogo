from assets.Const import WIN_WIDTH, WIN_HEIGHT
from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, WIN_HEIGHT)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, WIN_HEIGHT)))
                return list_bg