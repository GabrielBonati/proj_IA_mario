import retro
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

def play_agent():
    # Configurações do ambiente Retro Gym
    env = retro.make(game='SuperMarioWorld-Snes', state='YoshiIsland1', players=1)
    env = DummyVecEnv([lambda: env])

    # Carregar o modelo treinado
    model = DQN.load("mario_dqn_model")

    # Simulação do agente treinado
    obs = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)
        obs, _, done, _ = env.step(action)
        env.render()

if __name__ == "__main__":
    play_agent()
