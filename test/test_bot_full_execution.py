import time
import unittest
import asyncio
import keyboard
from Bot import Bot


class TestBotFullExecution(unittest.IsolatedAsyncioTestCase):
    async def test_execute_bot(self):
        # Arrange
        b = Bot()

        try:
            # Act
            bot_task = asyncio.create_task(b.execute_bot())

            # Assert
            # The task should not be completed immediately
            self.assertFalse(bot_task.done(), "Task started and closed right away!")

            time.sleep(1)

            # Ensure the task is still running after a short delay
            self.assertFalse(bot_task.done(), "Task started and closed before completing.")

            # Simulate pressing "ESC" to stop the bot
            keyboard.press("esc")
            keyboard.release("esc")

            # Allow some time for the task to process the ESC press
            await asyncio.sleep(0.2)

            # Ensure the task has ended
            self.assertTrue(bot_task.done(), "The bot task should have stopped after ESC was pressed.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed due to unexpected exception: {e}")