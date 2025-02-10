import time
import random

class UserScriptSimulator:
    def __init__(self, script_code):
        self.script_code = script_code
        self.simulated_elements = {}  # Dictionary to store simulated DOM elements

    def simulate_dom_query(self, selector):
      """Simulates document.querySelectorAll()."""
      matching_elements = []

      # In a real browser, this would query the DOM. Here we iterate our simulated elements.
      for element_id, element_data in self.simulated_elements.items():
          if self._element_matches_selector(element_data, selector):
              matching_elements.append(element_id) # Store the ID to represent the element.

      return matching_elements # Returns a list of matching element IDs.

    def _element_matches_selector(self, element_data, selector):
        """Rudimentary selector matching.  Needs improvement for complex selectors."""
        if selector == '*': # Matches all
            return True

        # Check for class names (e.g., ".className")
        if selector.startswith("."):
            class_name = selector[1:]
            return class_name in element_data.get("classes", [])

        # Check for tag names (e.g., "div")
        if selector.isalnum(): # Simple tag name check
            return element_data.get("tag", "").lower() == selector.lower()

        # Add more sophisticated selector checks here as needed (IDs, attributes, etc.)
        return False # Doesn't match if no conditions are met.

    def simulate_element_text_content(self, element_id):
        """Simulates accessing textContent."""
        element_data = self.simulated_elements.get(element_id)
        return element_data.get("text", "") if element_data else ""

    def simulate_element_set_text_content(self, element_id, new_text):
        """Simulates setting textContent."""
        element_data = self.simulated_elements.get(element_id)
        if element_data:
            element_data["text"] = new_text

    def simulate_mutation_observer(self, target_element_id, callback, options):
        """Simulates MutationObserver (very basic)."""
        # In a real browser, MutationObserver would asynchronously call the callback when changes occur.
        # This simulation just calls it periodically.
        while True:
            time.sleep(0.5)  # Simulate some time passing.
            callback() # Call the callback to mimic DOM changes.

    def simulate_set_timeout(self, callback, delay):
        """Simulates setTimeout."""
        time.sleep(delay / 1000) # Convert milliseconds to seconds
        callback()

    def add_simulated_element(self, element_id, tag, classes=None, text=""):
      """Adds a simulated DOM element."""
      self.simulated_elements[element_id] = {
            "tag": tag,
            "classes": classes or [],
            "text": text
        }


    def execute_script(self):
        """Executes the JavaScript code, simulating the browser environment."""
        # Replace the global functions in the script with our simulated versions.
        global document, window, setTimeout, MutationObserver # Make these available inside eval
        document = self  # 'document' is the simulator instance
        window = self # 'window' is the simulator instance
        setTimeout = self.simulate_set_timeout
        MutationObserver = type('MutationObserver', (), {'observe': lambda *args: self.simulate_mutation_observer(*args)}) # Stub class

        try:
          eval(self.script_code) # Run the script with our simulated globals.
        except Exception as e:
            print(f"Error executing script: {e}")


# Example usage:
javascript_code = """
  // ... (Your JavaScript code from before, with the Gemini refusal replacement) ...
"""

simulator = UserScriptSimulator(javascript_code)

# Add simulated elements to mimic the Gemini page structure.
simulator.add_simulated_element("gemini-response", "div", classes=["gemini-message"])
simulator.add_simulated_element("some-other-element", "p", text="This is some other text.")

simulator.execute_script()

print(simulator.simulate_element_text_content("gemini-response")) # Check the modified content.

