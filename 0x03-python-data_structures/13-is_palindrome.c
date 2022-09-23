#include "lists.h"

/**
 * len_listint - finds the length of a singly linked list.
 * @head: The address of the head of the linked list.
 * Return: The length of the linked list.
 */
int len_listint(listint_t **head)
{
	listint_t *current = *head;
	int len = 0;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	return (len);
}

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: The address of the start of the list to be reversed.
 * Return: A pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	current = prev;

	return (current);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: The address of the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 * Description: An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *reverse, *tmp, *current = *head;

	if (*head == NULL || head == NULL)
		return (1);

	len = len_listint(head);
	for (i = 0; i < len / 2; i++)
	{
		current = current->next;
	}

	reverse = reverse_listint(&current);
	tmp = reverse;

	current = *head;
	while (reverse)
	{
		if (current->n != reverse->n)
			return (0);

		current = current->next;
		reverse = reverse->next;
	}

	reverse_listint(&tmp);

	return (1);
}
